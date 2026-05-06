# Custom Wordle
My CS32 Final Project: **Custom Wordle**

I want to create a platform where 2 clients can play a custom wordle game against each other through a server.

**How to Play:**
The smart client sends any word.
The dumb client repeatedly guesses and sends their guess to the server which checks the guess against the secret.
The dumb client can also ask for a hint by inputting "hint please" which will not count as a turn, but will notify the smart client.
*In 3 separate terminals, start the server first, then smart client, input the secret word, then start the dumb client.*

**Citations:**
I referenced Generative AI (Claude) to learn how to connect 2 clients to a server using the socket library.

https://youtu.be/kjqNK3GbGEU
