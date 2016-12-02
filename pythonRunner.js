import cp from 'child_process';
import path from 'path';
import fs from 'fs';

console.log(path.resolve('pyScripts/hello_world.py'));
const spawn = cp.spawn('python', ['hello_world.py']);
let string = '';
let error = '';

spawn.stdout.on('data', (data) => (string += data));
spawn.stderr.on('data', (err) => {
  error += err;
  console.log('error: ', error)
});

spawn.on('close', (code) => console.log('string: ', string));
