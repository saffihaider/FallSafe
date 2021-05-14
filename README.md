## FallSafe

Fallsafe uses real-time video monitoring to estimate and classify poses using PosNet and a trained Teachable Machine neural network. We classified poses into two categories: Safe or Fallen down. If the user has fallen and stayed down, we send out an alert to their emergency contact.


# How we built it: #

We followed along with YoutTube videos and blog posts about ml5 projects and PosNet to get the framework of what we wanted to do. We then trained our neural network on teachable machine using a limited dataset of recorded video snapshots and images from datasets. Finally we integrated our neural network into the model, formatted our site on bootstrap, and combined our code to finally put the site together.

Challenges we ran into:

We ran into some challenges with our initial plans for audio in Javascript. We also were thrown for a few loops.

Accomplishments that we're proud of:

Learning! We all wanted to learn more about machine learning and we definitely got to do that while also getting to know each other and enjoy the experience.

What we learned:

There are MANY ways to integrate machine learning into code and these days it's incredibly accessible. Even from 2 years ago the resources have grown considerably to learn about and deploy these technologies.

What's next for Fall Safe:

Our demo shows the potential for integrations of this type to be widely distributed within homes of vulnerable communities. Before that can happen, we would need to ensure our model was trained on a larger dataset across many different locations with many different people so that it will be robust and helpful for anyone who wants to use it. As internet of things within the home becomes more popular, cameras will be able to send your google home or smart assistant of choice the alert that you have fallen down. Your smart assistant can then access your contacts, verbally ask if you're alright, or execute another specified safety protocol. If our validity and reliability becomes consistent enough to eliminate considerable risk of false alarms, we can think about offering direct access to emergency services.
