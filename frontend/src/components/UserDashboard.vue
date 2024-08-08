// UserDashboard.vue
<template>
  <div>
    <SignUp @userDataFetched="handleUserData"></SignUp>
    <div v-if="userData">
      <h1>Account Information</h1>
      <div v-for="account in userData.accounts" :key="account.id">
        <p><strong>Account:</strong> {{ account.iban }}</p>
        <p><strong>Balance:</strong> {{ account.balance }} {{ account.currency }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import SignUp from './SignUp.vue';

export default {
  components: {
    SignUp
  },
  data() {
    return {
      userData: null
    };
  },
  methods: {
    handleUserData(data) {
      this.userData = data;
    }
  }
}
</script>
