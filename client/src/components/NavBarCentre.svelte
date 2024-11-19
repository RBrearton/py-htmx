<script lang="ts">
  import { onMount } from "svelte";
  import NavBarButton from "./NavBarButton.svelte";

  // Make a typescript interface for the topic that we're fetching a list of.
  interface Topic {
    name: string;
  }
  let topics: Topic[] = [];

  // Fetch the topics from the server.
  onMount(async () => {
    const response = await fetch("/api/topics");
    topics = await response.json();

    // Log the topics to the console.
    console.log(topics);
  });
</script>

<div class="navbar-center">
  <NavBarButton text="Home" route="/" />
  {#each topics as topic}
    <NavBarButton text={topic.name} route={`/${topic.name.toLowerCase()}`} />
  {/each}
</div>
