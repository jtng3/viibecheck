<script lang="ts">
	import '../app.postcss';
</script>

<div class="flex flex-col min-h-screen w-full">
	<div
		class="bg-primary-700 h-[80px] w-full px-10 flex flex-row items-center justify-start gap-10 text-white"
	>
		<div class="font-bold text-xl tracking-widest">ViibeCheck</div>
		<a href="/">Home</a>
		<a href="/about">About</a>
		<a href="/search">Search</a>
		<a href="/new_report">New Report</a>
		<a href="/resources">Resources</a>
	</div>
	<main class="flex flex-col p-4 w-full max-w-5xl m-0 box-border">
		<slot />
	</main>
</div>
