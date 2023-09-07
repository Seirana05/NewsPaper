# @catch_db_exceptions
# async def process_messages(messages, do_async):
#     for message in messages:
#         user = get_user(message['user']['id'])
#         update_user_messages(user, message)
#         await process_message(message, do_async)
#         # we don't return message text here: just "OK"
#         # reasons are described in jira.project.com/browse/KEK-11829
#         return 200, 'OK'