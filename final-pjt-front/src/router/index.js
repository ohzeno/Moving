import Vue from "vue";
import VueRouter from "vue-router";
import Login from "@/views/accounts/Login.vue";
import Recommend from "@/components/Recommend.vue";
import Reviews from "@/views/community/Reviews.vue";
import CreateReview from "@/components/CreateReview.vue";
import ReviewDetail from "@/components/ReviewDetail.vue";
import UpdateReview from "@/components/UpdateReview.vue";
import Signup from "@/views/accounts/Signup.vue";
import Main from "@/views/home/Main.vue";
import MovieDetail from "@/views/home/MovieDetail.vue";
import MovieSearchResult from "@/views/home/MovieSearchResult.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Main",
    component: Main,
  },
  {
    path: "/movies",
    name: "MovieDetail",
    component: MovieDetail,
  },
  {
    path: "/accounts/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/accounts/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/movies/movie-search-result",
    name: "MovieSearchResult",
    component: MovieSearchResult,
  },
  {
    path: "/reviews",
    name: "Reviews",
    component: Reviews,
  },
  {
    path: "/createreview",
    name: "CreateReview",
    component: CreateReview,
  },
  {
    path: "/reviewdetail",
    name: "ReviewDetail",
    component: ReviewDetail,
  },
  {
    path: "/updatereview",
    name: "UpdateReview",
    component: UpdateReview,
  },
  {
    path: "/recommend",
    name: "Recommend",
    component: Recommend,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
