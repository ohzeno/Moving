<template>
  <div id="app">
    <!-- 네브바 -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-black">
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{ name: 'Main' }">
          <img
            class="mx-4"
            width="140px"
            height="70px"
            src="@/assets/logo2.png"
            alt="log"
          />
        </router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 fs-3">
            <li class="nav-item">
              <router-link
                class="nav-link acitve"
                aria-current="page"
                :to="{ name: 'Main' }"
                >Home</router-link
              >
            </li>
            <li class="nav-item">
              <router-link
                class="nav-link"
                aria-current="page"
                :to="{ name: 'Reviews' }"
                >Social</router-link
              >
            </li>
            <li class="nav-item">
              <router-link
                class="nav-link"
                aria-current="page"
                :to="{ name: 'Recommend' }"
                >Recommend</router-link
              >
            </li>
          </ul>
          <div class="mx-3 nav-item dropdown bg-light rounded my-2">
            <router-link
              class="nav-link dropdown-toggle"
              to="#"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              ><b-icon icon="person-fill"></b-icon> User
            </router-link>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <div v-if="this.$store.state.token">
                <button class="dropdown-item" @click="logout">Logout</button>
              </div>
              <div v-if="this.$store.state.token === null">
                <router-link class="dropdown-item" :to="{ name: 'Login' }"
                  >Login</router-link
                >
                <router-link class="dropdown-item" :to="{ name: 'Signup' }"
                  >Signup</router-link
                >
              </div>
            </div>
          </div>
          <small-Searchbar @search-movie="searchMovie"> </small-Searchbar>
        </div>
      </div>
    </nav>
    <!-- 라우터뷰 -->
    <router-view />
  </div>
</template>

<script>
import axios from "axios";
import SmallSearchbar from "@/components/SmallSearchbar.vue";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "App",
  components: {
    SmallSearchbar,
  },
  data: function () {
    return {
      inputData: null,
      movies: [],
      result: [],
    };
  },
  methods: {
    logout: function () {
      this.$store.state.user = null;
      localStorage.removeItem("jwt");
      this.$store.dispatch("logout");
      alert("You have successfully logged out");
      location.reload();
    },
    searchMovie: function (inputdata) {
      axios
        .get(`${SERVER_URL}/movies/find/${inputdata}`)
        .then((res) => {
          this.movies = res.data;
          this.$store.dispatch("searchMovie", this.movies);
        })
        .then(() => {
          this.$router.push({ name: "MovieSearchResult" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    const token = localStorage.getItem("jwt");
    if (token) {
      this.$store.dispatch("login");
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: #212529;
}

.navbar {
  z-index: 100;
}
html {
  background: #212529;
}
#nav {
  background-color: black;
  position: fixed;
  z-index: 100;
  top: 0;
  display: block;
  flex-direction: row;
  left: 0;
  width: 100%;
  font-size: 1.3rem;
  letter-spacing: 0.4px;
}

#navitem {
  margin-right: auto;
  margin-left: auto;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

body {
  margin: 0;
  padding: 0;
  background: #102a43;
  background-size: contain;
}
</style>
