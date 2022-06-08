/*
Create a queue with Kue
Create an object containing the Job data with the following format:
{
  phoneNumber: string,
  message: string,
}
Create a queue named push_notification_code, and create a job with the object created before
When the job is created without error, log to the console Notification job created: JOB ID
When the job is completed, log to the console Notification job completed
When the job is failing, log to the console Notification job failed
Nothing else will happen - to process the job, go to the next task!

If you execute multiple time this file, you will see the JOB ID increasing - it means you are storing new job to process…
*/
import kue from 'kue';
const queue = kue.createQueue();

const job = {
  phoneNumber: '',
  message: '',
}
const jobs = queue.create('push_notification_code', job).save((err) => {
  if(!err) console.log(`Notification job created: ${jobs.id}`);
})

jobs.on('complete', () => {
  console.log(' Job completed ');
}).on('failed', (err, done) => {
  console.log('Notification job completed');
})
