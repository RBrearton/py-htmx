<script>
  export let title;
  export let isPadded = true;
</script>

<!-- We wrap the title up in a prose block to improve the formatting/style. -->

{#if isPadded}
  <article class="prose px-5">
    <h4 class="text-primary-content">
      {title}
    </h4>
  </article>
{:else}
  <article class="prose">
    <h4 class="text-primary-content">
      {title}
    </h4>
  </article>
{/if}
