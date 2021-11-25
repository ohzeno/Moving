<template>
  <div>
    <h1 class="mt-3">Signup</h1>
    <div style="width: 400px; margin: 16px auto">
      <div style="width: 400px; margin: 8px auto">
        <label for="username" style="width: 200px">Username</label>
        <input
          class="rounded"
          type="text"
          id="username"
          v-model.trim="credentials.username"
          style="width: 200px"
        />
      </div>
      <div style="width: 400px; margin: 8px auto">
        <label for="password" style="width: 200px">Password</label>
        <input
          class="rounded"
          type="password"
          id="password"
          v-model="credentials.password"
          style="width: 200px"
        />
      </div>
      <div style="width: 400px; margin: 8px auto">
        <label for="passwordConfirmation" style="width: 200px"
          >Password confirmation</label
        >
        <input
          class="rounded"
          type="password"
          id="passwordConfirmation"
          v-model="credentials.passwordConfirmation"
          @keyup.enter="signup"
          style="width: 200px"
        />
      </div>
    </div>
    <b-button @click="signup" class="my-1">Sign-up</b-button>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Signup",
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
    };
  },
  methods: {
    signup: function () {
      if (
        this.credentials.username &&
        this.credentials.password &&
        this.credentials.passwordConfirmation
      ) {
        axios({
          method: "post",
          url: `${SERVER_URL}/accounts/signup/`,
          data: this.credentials,
        })
          .then((res) => {
            alert("Congratulate your joining");
            this.login(res);
          })
          .catch((err) => {
            alert(
              " There was an error processing your signup \n - Username is already taken  \n - Password and password confirmation do not match"
            );
            console.log(err);
          });
      } else {
        alert("There is an empty box.");
      }
    },
    login: function (res) {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/api-token-auth/",
        data: {
          username: res.data.username,
          password: this.credentials.password,
        },
      })
        .then((res) => {
          this.$store.state.user = this.credentials.username;
          localStorage.setItem("jwt", res.data.token);
          this.$store.dispatch("login");
          this.$router.go(-1);
        })
        .catch((err) => {
          alert("Please, Check your username or password.");
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
