function is_prime(n){
    if (n<2){
        return false;
    }

    for (let i =2; i<n; i++){
        if (n%i===0){
            return false;
        }
    }
return true;

}
const readline = require('readline').createInterface({
    input:process.stdin,
    output: process .stdout
});
 readline.question("Enter a number:", input => {
    const N = parseInt(input);

    console.log(`Prime number up to ${N} are:`);

    for (let i=2; i <=N; i++){
        if (is_prime(i)){
            process.stdout.write(i+ ' ');

        }
    }
    readline.close();
 });