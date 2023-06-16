<script lang="ts">
</script>

<svelte:head>
	<title>viibecheck</title>
	<meta name="New Report" content="New Report Page" />
</svelte:head>

<!-- Option A -->
<div class="pb-20">
	<div class="text-primary-600 text-xl font-bold pb-5">New Incident Report</div>
	<form class="grid grid-cols-1 gap-5">
		<div class="flex flex-row w-full gap-10">
			<input
				class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 w-full placeholder:text-primary-400"
				placeholder="First Name"
				type="text"
			/>
			<input
				class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 w-full placeholder:text-primary-400"
				placeholder="Last Name"
				type="text"
			/>
		</div>
		<div class="flex flex-row gap-10">
			<input
				placeholder="State"
				class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 w-full placeholder:text-primary-400"
				type="text"
			/>
			<input
				placeholder="Phone Number"
				class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 w-full placeholder:text-primary-400"
				type="text"
			/>
			<input
				placeholder="Incident Year"
				class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 w-full placeholder:text-primary-400"
				type="date"
			/>
		</div>
		<div class="flex flex-row w-full justify-around">
			<div class="flex flex-row items-center gap-4">
				<div>Work Related?</div>
				<input
					class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 placeholder:text-primary-400"
					type="checkbox"
				/>
			</div>
			<div class="flex flex-row items-center gap-4">
				<div>School Related?</div>
				<input
					class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 placeholder:text-primary-400"
					type="checkbox"
				/>
			</div>
		</div>
		<div class="flex flex-row w-full justify-around">
			<textarea
				placeholder="Add Specific Details? These are entirely optional."
				class="rounded-md focus:border-primary-400 focus:ring-0 border w-full text-gray-500 border-primary-600 placeholder:text-primary-400"
			/>
		</div>
		<div class="flex flex-row gap-10 justify-cstart">
			<button class="bg-primary-600 text-white px-4 py-2 rounded-md w-[100px]">Submit</button>
			<button
				class="bg-white text-primary-600 px-4 py-2 rounded-md w-[100px] border border-primary-600"
				>Reset</button
			>
		</div>
	</form>
</div>
