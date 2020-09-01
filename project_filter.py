import sys
from workflow import Workflow, ICON_WEB, web

from login import login


def main(wf):
    eid = login()
    url = 'http://codingcorp.coding.9.134.77.232.xip.io/api/project_recent_views/query'
    r = web.get(url, cookies=dict(
        enterprise_domain="codingcorp",
        eid = eid
    ))
    if r.status_code != 200:
        r.raise_for_status()
    pass

    data = r.json()['data']
    for project in data:
        wf.add_item(title=project['display_name'], args=project['id'])