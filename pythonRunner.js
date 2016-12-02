import cp from 'child_process';
import path from 'path';
import fs from 'fs';

const spawn = cp.spawn('python', ['pyScripts/forLoop.py']);
let string = '';
let error = '';

spawn.stdout.on('data', (data) => (string += data));
spawn.stderr.on('data', (err) => {
  error += err;
  console.log('error: ', error)
});

spawn.on('close', (code) => console.log('string: ', string));
