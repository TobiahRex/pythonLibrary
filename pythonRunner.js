import { spawn, exec } from 'child_process';
import colors from 'colors';

exec(
  'python pyScripts/arrays.py',
  // 'python algos/python/rota.py',
  (err, data) => {
  if (err) {
      process.stdout.write('\n');
      process.stdout.write(`❌  ${err}
  `.red);
      throw err;
    } else {
      process.stdout.write('\n');
      process.stdout.write(data.bold.green);
      process.stdout.write('\n');
    }
});

// const py = spawn('python', ['pyScripts/binaryNhex.py']);
// let string = '';
// let error = '';
//
// py.stdout.on('data', (data) => (string += data));
// py.stderr.on('data', (err) => {
//   error += err;
//   console.log('error: ', error)
// });
//
// py.on('close', (code) => {
//   console.log('result: \n', string)
// });
