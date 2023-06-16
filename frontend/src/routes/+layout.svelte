<script lang="ts">
	import '../app.postcss';
</script>

<div class="grid grid-cols-1 min-w-screen min-h-screen bg-primary-100 items-start">
	<div class="relative w-full flex flex-col justify-self-center justify-center">
		<div
			class="static bg-primary-700 h-[80px] w-full px-10 flex flex-row items-center justify-center gap-10 text-white"
		>
			<div class="font-bold text-xl tracking-widest">ViibeCheck</div>
			<a class="hover:text-white/50" href="/">Home</a>
			<a class="hover:text-white/50" href="/about">About</a>
			<a class="hover:text-white/50" href="/search">Search</a>
			<a class="hover:text-white/50" href="/new_report">New Report</a>
			<a class="hover:text-white/50" href="/resources">Resources</a>
		</div>
		<main class="flex w-full p-10 justify-center">
			<!-- Border is only for temporary vision of how we move items within the page -->
			<div class="grid grid-cols-1 w-full max-w-6xl border bg-white p-10">
				<slot />
			</div>
		</main>
	</div>
</div>
