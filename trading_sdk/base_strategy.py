from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional

from trading_sdk.structs import AccountData, OrderSignal


class BaseStrategy(ABC):
    def __init__(self, params: Optional[Dict[str, Any]] = None) -> None:
        self.config: Dict[str, Any] = {}
        self.params: Dict[str, Any] = self.default_params()
        if params:
            self.params.update(params)
        self.state: Dict[str, Any] = {}
        self.adapter: Optional[Any] = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self._logger_configured = False

    def setup(self, config: Dict[str, Any]) -> None:
        self.config = config
        self._configure_logger(config)

    def set_adapter(self, adapter: Any) -> None:
        self.adapter = adapter

    def update_params(self, overrides: Dict[str, Any]) -> None:
        self.params.update(overrides)

    def default_params(self) -> Dict[str, Any]:
        return {}

    def _configure_logger(self, config: Dict[str, Any]) -> None:
        if self._logger_configured:
            return

        log_cfg = config.get("logging", {}) if config else {}
        level_name = log_cfg.get("level", "INFO")
        level = logging.getLevelName(level_name)
        if isinstance(level, str):
            level = logging.INFO

        self.logger.setLevel(level)
        self.logger.propagate = False

        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        if not self.logger.handlers:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

            log_path = log_cfg.get("path")
            log_dir = log_cfg.get("dir", "logs")
            log_file = log_cfg.get("file", f"{self.__class__.__name__}.log")
            if log_path:
                path = Path(log_path)
            else:
                path = Path(log_dir) / log_file
            path.parent.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(path, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        self._logger_configured = True

    @abstractmethod
    def next_signal(self, market_data: Any, account_data: AccountData) -> OrderSignal:
        raise NotImplementedError
