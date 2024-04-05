from typing import Literal
from datetime import datetime
from database.wrapper import DB


def log(
	ip: str,
	endpoint: Literal['read_logs', 'dash', 'ping', 'echo', 'delete_all_logs'],
	params: dict[str, str] = {}
):
	with DB('src/database/archives/logs.json') as db:
		db.insert(({ # type: ignore
			"timestamp": str(datetime.now()),
			"ip": ip,
			"endpoint": endpoint,
			"params": params
		}))

