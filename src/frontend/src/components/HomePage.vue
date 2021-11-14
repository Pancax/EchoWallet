<template>
  <div class="main-container container">
    <div class="container sign-up">
      <button class="echo-btn sign-up-btn btn">
        <span>Login</span>
      </button>
      <button class="echo-btn sign-up-btn btn">
        <span>Sign Up</span>
      </button>
    </div>
    <div class="hero-container container">
      <h1 class="justify-content-center align-self-center title-text">
        EchoWallet
        <h4 class="font-italic tag-text">Make Sound Investments</h4>
        <a href="#about"
          ><button class="echo-btn call-action-btn btn" href="#about">
            <span>Learn More</span>
          </button></a
        >
      </h1>
    </div>
  </div>
  <div id="about" class="about-container">
    <div class="about-desc container">
      <div class="row">
        <div class="about-img-wrapper col">
          <img src="..\assets\logo.png" alt="" style="width: 500px" />
        </div>
        <div class="about-content col">
          <h1>What is EchoWallet?</h1>
          <span>
            EchoWallet is an automatic investment portfolio manager that
            picks stocks based on social media trends. It uses data analysis and
            web scraping to choose stocks, make predictions and make YOU money!
          </span>
        </div>
      </div>
    </div>
    <div class="cards container">
      <div class="row justify-content-around">
        <div class="card col-3" style="width: 18rem">
          <img
            class="card-img-top"
            src="..\assets\logo.png"
            alt="Card image cap"
          />
          <div class="card-body">
            <p class="card-text">
              Automatic Portfolio Management
            </p>
          </div>
        </div>
        <div class="card col-3" style="width: 18rem">
          <img
            class="card-img-top"
            src="..\assets\logo.png"
            alt="Card image cap"
          />
          <div class="card-body">
            <p class="card-text">
              Statistics-backed Stock Choices
            </p>
          </div>
        </div>
        <div class="card col-3" style="width: 18rem">
          <img
            class="card-img-top"
            src="..\assets\logo.png"
            alt="Card image cap"
          />
          <div class="card-body">
            <p class="card-text">
              Security In Numbers
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.main-container {
  height: 100vh;
}
.hero-container {
  padding-top: 300px;
}
.about-container {
  background-color: white;
}
.about-desc {
  height: 100vh;
  display: flex;
  align-items: center;
}
.about-content {
  padding-top: 30px;
  color: var(--bs-body-color);
}
.about-content h1 {
  margin-bottom: 30px;
}
.about-content span {
  font-size: 26px;
}
.cards {
  padding: 50px 0;
}
.card {
  font-size: 22px;
  background-color: transparent !important;
  border: none !important;
}
.card-text {
  color: blueviolet;
}
.title-text {
  font-size: 64px;
}
.call-action-btn {
  margin-top: 40px;
  width: 300px;
  height: 100px;
}
.call-action-btn span {
  font-size: 36px;
}
.sign-up {
  position: fixed;
  right: 5%;
  top: 2%;
}
.sign-up-btn {
  height: 60px;
  width: 120px;
  float: right;
  margin-left: 10px;
}
.sign-up-btn span {
  font-size: 20px;
}
.echo-btn {
  color: blueviolet !important;
  border-color: blueviolet !important;
}
.echo-btn:hover {
  background-color: blueviolet;
  color: white !important;
  transition-duration: 0.5s;
}
</style>
