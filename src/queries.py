"""
Author: Yash Singh Chauhan yashsinghchauhanformal@gmail.com
queries.py (c) 2023
Desc: This file includes all graphql queries to be modified and executed on Burpsuite Enterprise Server.
"""

START_SCAN = """
 mutation CreateScheduleItem {
    create_schedule_item(input: {site_id: "{SITE_ID}", scan_configuration_ids: ["{CONFIG_ID}"]}) {
        schedule_item {
            id
            site {
                name
            }
        }
    }
    }
"""

FOLDER_TREE = """
query SitesAndFolderInfo {
  site_tree {
    folders {
      id
      parent_id
      name
    }
  }
}
"""

GET_SCAN_CONFIGS = """
 query GetScanConfigurations {
    scan_configurations {
        id
        name
    }
    }
"""

GET_SCAN_METRICS = """
 query GetScanMetrics {
    scan(id: {SCANID}) { 
      scan_metrics {
        crawl_and_audit_progress_percentage
      }
    }
    }
"""

SITE_TREE =  """
    query GetSiteTree {
    site_tree {
        sites {
            id
            name
            scope {
                included_urls
                excluded_urls
            }
            application_logins {
                login_credentials {
                    label
                    username
                }
                recorded_logins {
                    label
                }
            }
        }
        folders {
            id
            name
        }
    }
}
  """


CANCEL_SCAN = """
mutation CancelScan($input: CancelScanInput!) {
  cancel_scan(input: $input) {
    {ID}
  }
}
"""


# To make folder root level, ID Must be 0
CREATE_FOLDER = """
mutation { 
    create_folder(input: {
    name: "{NAME}",
    parent_id: "{PARENT_ID}"
  }) {
    folder {
      id
      name
      parent_id
    }
  }
}
"""

# Get Scans and their IDS
GET_SCANS = """
query GetScan {
        scans {
            id
            status
            site_id
        }   
        }
"""
# Get Scan information by ID
GET_SCAN = """
 query GetScan {
        scan(id: {SCAN_ID}) {
            id
            status
            site_name
            start_time
            end_time
            scan_metrics {
                crawl_and_audit_progress_percentage
            }
        }   
        }
"""

GET_REPORT = """
query Report {
    scan_report(
      scan_id: {SCAN_ID}) {
    report_html
  }
}
"""

NEW_SITE = """
 mutation CreateSite {
 create_site(input: {name: "{SITENAME}", parent_id: {PARENT_ID}, application_logins: {login_credentials: [], recorded_logins: []} , scope: {included_urls: "{SITENAME}"}}) {
   site {
     id
     parent_id
     scope {
       included_urls
     }
     }
 }
}
  """