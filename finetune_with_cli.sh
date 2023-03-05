# upload data and create fine-tune job 
openai api fine_tunes.create -t example_data/faq.jsonl -m curie --suffix "my-faq"
# follow the fine-tune job status
openai api fine_tunes.follow -i <JOB_ID>
# get the finetune job status and if the finetuned finished you'll see your model name
openai api fine_tunes.get -i <JOB_ID>
