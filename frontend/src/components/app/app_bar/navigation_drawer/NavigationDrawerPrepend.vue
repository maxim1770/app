<template v-slot:prepend>
  <v-list>
    <v-list-item
      :to="{ name: 'main' }"
      title="Православие в Рукописях"
      subtitle="Выдержки из Рукописей до 1597 года"
      lines="two"
      color="blue-lighten-1"
    >
      <template v-slot:prepend>
        <v-icon
          icon="custom:OrthodoxCross"
          size="x-large"
        />
      </template>
    </v-list-item>
  </v-list>
</template>

<script>


export default {};

</script>



