def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)-1):
        b_der = len(nums)-1
        while i <= b_der:
            res = nums[i] + nums[b_der]
            if res == target and i != b_der:
                return [i, b_der]
            else:
                b_der -= 1


pruebas = [[2,7,11,15],[3,2,4],[3,3]]
targets = [9, 6, 6]

for prueba in zip(pruebas, targets):
    print(twoSum(prueba[0], prueba[1]))