# export OPENAI_API_KEY="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"
import openai

openai.api_key = ("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")

def create_training_file(file_path):
    file = openai.File.create(
        file = open(file_path, "rb"),
        purpose='fine-tune'
    )
    return file

# upload_response = create_training_file("jacobido_prepared.jsonl")
# print(upload_response)
# training_id = upload_response['id']
# fine_tuned_model = openai.FineTune.create(training_file=training_id, model='davinci')
# print(fine_tuned_model)

# print(openai.FineTune.list_events(id="ft-Z8j3C7L8OCJd6BWSsTc9c1IC"))
print(openai.FineTune.list_events(id="ft-xGW6tsfyDRYX2EXtNZTzo6sv"))
