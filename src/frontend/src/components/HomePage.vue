<template>
  <div class="main-container container">
    <!-- Modal -->
    <div
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Login Form</h5>
            <button
              type="button"
              id="closeModalBtn"
              ref="closeModalBtn"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label"
                  >Email address</label
                >
                <input
                  v-model="email"
                  type="email"
                  class="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                />
              </div>
              <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label"
                  >Password</label
                >
                <input
                  v-model="value"
                  type="password"
                  class="form-control"
                  id="exampleInputPassword1"
                />
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button @click="login()" class="btn btn-primary">Login</button>
          </div>
        </div>
      </div>
    </div>
    <div class="container sign-up">
      <button
        type="button"
        class="echo-btn sign-up-btn btn"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
      >
        <span>Login</span>
      </button>
    </div>
    <div class="hero-container container">
      <div class="container" style="width: 80%; margin-right: 40%">
        <div class="row justify-content-center">
          <h1 class="col align-self-center title-text">
            EchoWallet
            <h4 class="font-italic tag-text">Make Sound Investments</h4>
            <a href="#about"
              ><button class="echo-btn call-action-btn btn" href="#about">
                <span>Learn More</span>
              </button></a
            >
          </h1>
          <div class="col">
            <img src="..\assets\betterlogo.png" alt="" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <div id="about" class="about-container">
    <div class="about-desc container">
      <div class="row">
        <div class="about-img-wrapper col">
          <img src="..\assets\chart.png" alt="" style="width: 500px" />
        </div>
        <div class="about-content col">
          <h1>What is EchoWallet?</h1>
          <span>
            EchoWallet is an automatic investment portfolio manager that picks
            stocks based on social media trends. It uses data analysis and web
            scraping to choose stocks, make predictions and make YOU money!
          </span>
        </div>
      </div>
    </div>
    <div class="cards container">
      <h1 style="color: black">Cool Features</h1>
      <div class="row justify-content-around">
        <div class="card col-3" style="width: 18rem">
          <img
            class="card-img-top"
            src="..\assets\gear.png"
            alt="Card image cap"
          />
          <div class="card-body">
            <p class="card-text">Automatic Portfolio Management</p>
          </div>
        </div>
        <div class="card col-3" style="width: 18rem">
          <img
            class="card-img-top"
            src="..\assets\smort.png"
            alt="Card image cap"
          />
          <div class="card-body">
            <p class="card-text">Statistics-backed Stock Choices</p>
          </div>
        </div>
        <div class="card col-3" style="width: 18rem">
          <img
            class="card-img-top"
            src="..\assets\together.png"
            alt="Card image cap"
          />
          <div class="card-body">
            <p class="card-text">Security In Numbers</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      popToggle: false,
      email: '',
      value: '',
    };
  },
  methods: {
    popup() {
      this.popToggle = true;
    },
    login() {
      if (this.email == 'cool@email.com' && this.value == '123pass') {
        this.$refs.closeModalBtn.click();
        this.$emit('login_event', true);
      }
    },
  },
};
</script>

<style>
.main-container {
  height: 100vh;
}
.hero-container {
  padding-top: 150px;
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
  padding-top: 130px;
  color: var(--bs-body-color);
}
.about-content h1 {
  margin-bottom: 30px;
}
.about-content span {
  font-size: 26px;
}
.cards {
  padding-bottom: 100px;
  margin-bottom: 100px;
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
