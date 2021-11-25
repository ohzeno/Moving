<template>
  <b-container>
    <div>
      <br />
      <h2>Reviews</h2>
      <b-button
        v-if="this.$store.state.token"
        @click="toCreateReview()"
        class="my-2"
      >
        Create review
      </b-button>
      <br />
      <div class="listWrap bg-light text-dark rounded p-3">
        <table class="tbList" width="100%">
          <colgroup>
            <col width="6%" />
            <col width="*%" />
            <col width="40%" />
            <col width="15%" />
            <col width="15%" />
          </colgroup>
          <tr>
            <th>No.</th>
            <th>Movie title</th>
            <th>title</th>
            <th>Writer</th>
            <th>Updated_at</th>
          </tr>
          <!-- 리뷰가 있으면 -->
          <tr
            v-for="review in computedReviews"
            :key="review.id"
            @click="toDetail(review.id)"
          >
            <td>{{ review.id }}</td>
            <td>{{ review.movie_title }}</td>
            <td class="txt_left">
              <div>
                {{ review.title }}
              </div>
            </td>
            <td>{{ review.userName }}</td>
            <td>
              {{ review.updated_at.substr(0, 4) }}/{{
                review.updated_at.substr(5, 2)
              }}/{{ review.updated_at.substr(8, 2) }}.
              {{ review.updated_at.substr(11, 5) }}
            </td>
          </tr>
          <!-- 리뷰가 없을경우 -->
          <tr v-if="computedReviews.length == 0">
            <td colspan="4">There is no review.</td>
          </tr>
        </table>
      </div>
    </div>
  </b-container>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Reviews",
  data: function () {
    return {
      currentPage: 1,
      reviews: [],
      user: "",
    };
  },
  methods: {
    getReviews: function () {
      axios({
        method: "get",
        url: `${SERVER_URL}/community/`,
      })
        .then((res) => {
          this.reviews = res.data;
          this.reviews.reverse();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    toCreateReview: function () {
      if (localStorage.getItem("jwt")) {
        this.$store.dispatch("noTitle");
        this.$router.push({ name: "CreateReview" });
      } else {
        this.$router.push({ name: "Login" });
      }
    },
    toDetail: function (review_id) {
      if (localStorage.getItem("jwt")) {
        this.$store.dispatch("toDetail", review_id);
        this.$router.push({ name: "ReviewDetail" });
      } else {
        this.$router.push({ name: "Login" });
      }
    },
  },
  created: function () {
    this.getReviews();
  },
  computed: {
    computedReviews: function () {
      return this.reviews;
    },
  },
};
</script>

<style scoped>
.searchWrap {
  border: 1px solid #888;
  border-radius: 5px;
  text-align: center;
  padding: 20px 0;
  margin-bottom: 40px;
}
.searchWrap input {
  width: 60%;
  height: 36px;
  border-radius: 3px;
  padding: 0 10px;
  border: 1px solid #888;
}
.searchWrap .btnSearch {
  display: inline-block;
  margin-left: 10px;
}
.tbList th {
  border-top: 1px solid #888;
}
.tbList th,
.tbList td {
  border-bottom: 1px solid #eee;
  padding: 5px 0;
}
.tbList td.txt_left {
  text-align: left;
}
.btnRightWrap {
  text-align: right;
  margin: 10px 0 0 0;
}

.pagination {
  margin: 20px 0 0 0;
  text-align: center;
}
.first,
.prev,
.next,
.last {
  border: 1px solid #666;
  margin: 0 5px;
}
.pagination span {
  display: inline-block;
  padding: 0 5px;
  color: #333;
}
.pagination a {
  text-decoration: none;
  display: inline-blcok;
  padding: 0 5px;
  color: #666;
}
</style>
