<template>
  <div>
    <h1 class="mt-3">Login</h1>
    <div style="width: 300px; margin: 16px auto">
      <div style="width: 300px; margin: 8px auto">
        <label for="username" style="width: 100px">Username</label>
        <input
          type="text"
          id="username"
          v-model="credentials.username"
          class="rounded"
          style="width: 200px"
        />
      </div>
      <div style="width: 300px; margin: 8px auto">
        <label for="password" style="width: 100px">Password</label>
        <input
          type="password"
          id="password"
          v-model="credentials.password"
          @keyup.enter="login"
          class="rounded"
          style="width: 200px"
        />
      </div>
    </div>
    <b-button @click="login" class="mx-1">login</b-button>
    <b-button @click="moveToSignUp">sign up</b-button>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Login",
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
    };
  },
  methods: {
    login: function () {
      axios({
        method: "post",
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: this.credentials,
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
    moveToSignUp: function () {
      this.$router.push({ name: "Signup" });
    },
  },
};
</script>

<style></style>
