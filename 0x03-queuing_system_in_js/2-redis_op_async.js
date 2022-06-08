import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
client.on('error', (err) => console.log('Redis client not connected to the server:', err));

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value).then((reply) => {
    redis.print(`Reply: ${reply}`)
  })
}
async function displaySchoolValue(schoolName) {
  console.log(await getAsync(schoolName))
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
