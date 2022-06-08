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
