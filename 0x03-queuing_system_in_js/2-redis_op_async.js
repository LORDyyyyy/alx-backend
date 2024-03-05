import redis from 'redis';
import { promisify } from 'util';

let client = redis.createClient({ url: 'redis://localhost:6379' });

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

const clientGetAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
        let out = await clientGetAsync(schoolName);
        console.log(out);
    } catch (error) {
        console.log(error.message);
    }
}

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
