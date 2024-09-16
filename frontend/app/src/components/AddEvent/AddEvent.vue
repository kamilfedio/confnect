<template>
  <div class="addEventDialog">
    <div class="addEventDialog__title">Add event</div>
    <form class="addEventDialog__form" @submit.prevent="submitForm">
      <input class="addEventDialog__input" type="text" v-model="name" placeholder="Event name..." />
      <input class="addEventDialog__input" type="datetime-local" v-model="date" />
      <textarea
        class="addEventDialog__textarea"
        type="text"
        v-model="description"
        placeholder="Description..."
      />
      <input class="addEventDialog__input" type="text" v-model="place" placeholder="Place..." />
      <input
        class="addEventDialog__input"
        type="text"
        v-model="optional_info"
        placeholder="Location..."
      />
      <button class="addEventDialog__button" type="submit">Add Event</button>
    </form>
    <v-icon class="addEventDialog__icon" @click="closeDialog">mdi-close</v-icon>
  </div>
</template>

<script src="./AddEvent.vue.ts"></script>
<style src="./AddEvent.scss" scoped></style>
