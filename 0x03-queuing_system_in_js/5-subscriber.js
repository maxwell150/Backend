/*
On connect, it should log the message Redis client connected to the server
On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
It should subscribe to the channel holberton school channel
When it receives message on the channel holberton school channel, it should log the message to the console
When the message is KILL_SERVER, it should unsubscribe and quit
*/
import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});
subscriber.on("connect", () => {
  console.log("Redis client connected to the server");
});

subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});

subscriber.subscribe('holberton school channel');
