/*
In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value

Create Hash:
Using hset, let’s store the following:

The key of the hash should be HolbertonSchools
It should have a value for:
Portland=50
Seattle=80
New York=20
Bogota=20
Cali=40
Paris=2
Make sure you use redis.print for each hset
Display Hash:
Using hgetall, display the object stored in Redis. It should return the following:

Requirements:

Use callbacks for any of the operation, we will look at async operations later
*/
import redis from 'redis';

const client = redis.createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, k) => {
  client.hset('HolbertonSchools', key, values[k], redis.print);
});

client.hgetall('HolbertonSchools', (err, value) => {
  console.log(value);
})
