import cp from 'child_process';
const spawn = cp.spawn('python', ['pyScripts/hello_world.py']);
let string = '';
let error = '';

spawn.stdout.on('data', (data) => (string += data));
spawn.stderr.on('data', (error) => console.log('stderr: ', error));

spawn.on('close', (code) => console.log('string: ', string));