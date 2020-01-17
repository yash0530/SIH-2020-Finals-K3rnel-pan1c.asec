import requests
from pprint import pprint

def allIssuesByProject(p_name):
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/search?jql=project={}'.format(p_name), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    data = r.json()
    html = "<div class='container p-4'><h1>Issues for Project: {}</h1>".format(p_name)
    for issue in data["issues"]:
        html += '''
            <div class="card p-4 mt-4" style="display: block; width: 25rem;">
                <h3>{}</h3>
                <hr>
                <div><b>Reporter:</b> {}</div>
                <div><b>Assignee:</b> {}</div>
                <div><b>Status:</b> {}</div>
                <div><b>Key:</b> {}</div>
                <div><b>Priority:</b> {}</div>
                <div><b>Watches:</b> {}</div>
                <div><b>Created:</b> {}</div>
            </div>
        '''.format(issue["fields"]["summary"], issue["fields"]["reporter"]["displayName"], "Not Assigned" if (type(issue["fields"]["assignee"]) == type(None)) else issue["fields"]["assignee"]["displayName"], \
            issue["fields"]["status"]["name"], issue["key"], issue["fields"]["priority"]["name"], issue["fields"]["watches"]["watchCount"], \
                issue["fields"]["created"])
    html += "</div>"
    return html

def allIssuesByProjectAndIssueType(p_name, i_type):
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/search?jql=project={}'.format(p_name), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    data = r.json()
    html = "<div class='container p-4'><h1>Issues for Project: {}</h1>".format(p_name)
    for issue in data["issues"]:
        if (issue["fields"]["status"]["name"] == i_type):
            html += '''
                <div class="card p-4 mt-4" style="display: block; width: 25rem;">
                    <h3>{}</h3>
                    <hr>
                    <div><b>Reporter:</b> {}</div>
                    <div><b>Assignee:</b> {}</div>
                    <div><b>Status:</b> {}</div>
                    <div><b>Key:</b> {}</div>
                    <div><b>Priority:</b> {}</div>
                    <div><b>Watches:</b> {}</div>
                    <div><b>Created:</b> {}</div>
                </div>
            '''.format(issue["fields"]["summary"], issue["fields"]["reporter"]["displayName"], "Not Assigned" if (type(issue["fields"]["assignee"]) == type(None)) else issue["fields"]["assignee"]["displayName"], \
                issue["fields"]["status"]["name"], issue["key"], issue["fields"]["priority"]["name"], issue["fields"]["watches"]["watchCount"], \
                    issue["fields"]["created"])
    html += "</div>"
    return html

def allIssuesByAssigneeAndIssueType(assignee, i_type):
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee={}'.format(assignee), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    data = r.json()
    html = "<div class='container p-4'><h1>Issues for Assignee: {}</h1>".format(assignee)
    for issue in data["issues"]:
        if (issue["fields"]["status"]["name"] == i_type):
            html += '''
                <div class="card p-4 mt-4" style="display: block; width: 25rem;">
                    <h3>{}</h3>
                    <hr>
                    <div><b>Reporter:</b> {}</div>
                    <div><b>Assignee:</b> {}</div>
                    <div><b>Status:</b> {}</div>
                    <div><b>Key:</b> {}</div>
                    <div><b>Priority:</b> {}</div>
                    <div><b>Watches:</b> {}</div>
                    <div><b>Created:</b> {}</div>
                </div>
            '''.format(issue["fields"]["summary"], issue["fields"]["reporter"]["displayName"], "Not Assigned" if (type(issue["fields"]["assignee"]) == type(None)) else issue["fields"]["assignee"]["displayName"], \
                issue["fields"]["status"]["name"], issue["key"], issue["fields"]["priority"]["name"], issue["fields"]["watches"]["watchCount"], \
                    issue["fields"]["created"])
    html += "</div>"
    return html

def allIssuesByAssigneeAndProjectName(assignee, p_name):
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee={}&'.format(assignee), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    data = r.json()
    html = "<div class='container p-4'><h1>Issues for Assignee: {}</h1>".format(assignee)
    for issue in data["issues"]:
        if (issue["fields"]["name"] == p_name):
            html += '''
                <div class="card p-4 mt-4" style="display: block; width: 25rem;">
                    <h3>{}</h3>
                    <hr>
                    <div><b>Reporter:</b> {}</div>
                    <div><b>Assignee:</b> {}</div>
                    <div><b>Status:</b> {}</div>
                    <div><b>Key:</b> {}</div>
                    <div><b>Priority:</b> {}</div>
                    <div><b>Watches:</b> {}</div>
                    <div><b>Created:</b> {}</div>
                </div>
            '''.format(issue["fields"]["summary"], issue["fields"]["reporter"]["displayName"], "Not Assigned" if (type(issue["fields"]["assignee"]) == type(None)) else issue["fields"]["assignee"]["displayName"], \
                issue["fields"]["status"]["name"], issue["key"], issue["fields"]["priority"]["name"], issue["fields"]["watches"]["watchCount"], \
                    issue["fields"]["created"])
    html += "</div>"
    return html

def allIssuesByAssigneeProjectNameAndIssueType(assignee, p_name, i_type):
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/search?jql=assignee={}'.format(assignee), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    data = r.json()
    html = "<div class='container p-4'><h1>Issues for Assignee: {}</h1>".format(assignee)
    for issue in data["issues"]:
        if (issue["fields"]["name"] == p_name and issue["fields"]["status"]["name"] == i_type):
            html += '''
                <div class="card p-4 mt-4" style="display: block; width: 25rem;">
                    <h3>{}</h3>
                    <hr>
                    <div><b>Reporter:</b> {}</div>
                    <div><b>Assignee:</b> {}</div>
                    <div><b>Status:</b> {}</div>
                    <div><b>Key:</b> {}</div>
                    <div><b>Priority:</b> {}</div>
                    <div><b>Watches:</b> {}</div>
                    <div><b>Created:</b> {}</div>
                </div>
            '''.format(issue["fields"]["summary"], issue["fields"]["reporter"]["displayName"], "Not Assigned" if (type(issue["fields"]["assignee"]) == type(None)) else issue["fields"]["assignee"]["displayName"], \
                issue["fields"]["status"]["name"], issue["key"], issue["fields"]["priority"]["name"], issue["fields"]["watches"]["watchCount"], \
                    issue["fields"]["created"])
    html += "</div>"
    return html

def issueByIssueKey(i_key):
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/issue/{}'.format(i_key), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    issue = r.json()
    html = "<div class='container p-4'><h1>Issue for ID: {}</h1>".format(i_key)
    html += '''
        <div class="card p-4 mt-4" style="display: block; width: 40rem;">
            <h3>{}</h3>
            <hr>
            <div><b>Reporter:</b> {}</div>
            <div><b>Assignee:</b> {}</div>
            <div><b>Status:</b> {}</div>
            <div><b>Priority:</b> {}</div>
            <div><b>Watches:</b> {}</div>
            <div><b>Created:</b> {}</div>
    '''.format(issue["fields"]["summary"], issue["fields"]["reporter"]["displayName"], "Not Assigned" if (type(issue["fields"]["assignee"]) == type(None)) else issue["fields"]["assignee"]["displayName"], \
        issue["fields"]["status"]["name"], issue["fields"]["priority"]["name"], issue["fields"]["watches"]["watchCount"], \
            issue["fields"]["created"])

    # description
    html += "<hr><div><b>Description</b></div><div>"
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/issue/{}?fields=description'.format(i_key), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    if (type(r.json()["fields"]["description"]) == type(None)):
        html += "Not Available"
    else:
        html += r.json()["fields"]["description"]
    html += "</div>"

    # attachments
    html += "<hr><div><b>Attachments</b></div><div>"
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/issue/{}?fields=attachment'.format(i_key), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    attachments = r.json()
    for attach in attachments["fields"]["attachment"]:
        html += "<li><a href='{}'>{}</a>".format(attach["content"], attach["filename"]) + "</li>"
    html += "</div>"

    # comments
    html += '<hr><div><b>Comments</b></div><div class="jumbotron mt-2" style="padding: 20px;"><div><div style="display: flex; justify-content: space-between;">'
    r = requests.get('https://kernel-panic.atlassian.net/rest/api/2/issue/{}/comment'.format(i_key), \
        auth=('yashjain0530@gmail.com', 'Pt6yTlLgfFeNjvBOnSeL32B1'))
    comments = r.json()
    for comment in comments["comments"]:
        html += '<span><b>{}</b></span>'.format(comment["author"]["displayName"])
        html += '<span style="color: gray;">{}</span></div>'.format(comment["created"][:10])
        html += '<div>{}</div><hr></div>'.format(comment["body"])

    return html