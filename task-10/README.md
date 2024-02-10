## RustOS
- This task is bit harder for me. I dont know where to start in this particular task.
- Reference material helped me a lot in this particular task.
- I haven't learned rust well but I can understand the code what it was written.
-  I found a lot of syntax error in this code like adding  semicolon ";"
- GOOGLE helped me a lot in facing the error which I'm getting  while running the program.
 
I changed the color in as given in the output.
 
## Problems faced during solving the problem
- when i tried to execute in the vscode using ```cargo run```in terminal I faced this error:
```
Finished release [optimized + debuginfo] target(s) in 0.07s
Running: `qemu-system-x86_64 -drive format=raw,file=target/x86_64-rusk/debug/bootimage-rusk_os.bin`
qemu-system-x86_64: symbol lookup error: /snap/core20/current/lib/x86_64-linux-gnu/libpthread.so.0: undefined symbol: __libc_pthread_init, version GLIBC_PRIVATE

```
- Then i tried to run the entire code in my ubuntu terminal, Finally the out came.
- But i cannot enter the password `amfoss`. It took in reverse. 
 I used the for loop to order the password> I found the for loop in the `interrupt.rs`

 ```

    for i in COUNT..ARRAY_SIZE {
        let index = i;
        if chars[index].is_none() {
            COUNT += 1;
            chars[index] = Some(character);
            return Ok(());
        }
    }


 ``` 

Finally i got the HEADPAD

