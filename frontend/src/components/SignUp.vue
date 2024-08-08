// SignUp.vue
<template>
  <div>
    <button @click="fetchUserData">Fetch User Data from LHV</button>
  </div>
</template>

<script>
export default {
  methods: {
    fetchUserData() {
      fetch('http://localhost:5000/user-data', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          alert(data.error);
        } else {
          this.$emit('userDataFetched', data);
        }
      });
    }
  }
}
</script>