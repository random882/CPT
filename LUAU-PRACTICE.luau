-- Studio game development practice

local tool = script.Parent
local remote = tool:WaitForChild("Activate")

local Grab_range = 10
local Damage = 25
local Cooldown = 3

local debounce = {}

local function find_target(player)
	local char = player.Character
	if not char then return end

	local root = char:FindFirstChild("HumanoidRootPart")
	if not root then return end

	local closest = nil
	local dist = Grab_range

	for _, i in pairs(game.Players:GetPlayers()) do
		if i ~= player and i.Character and v.Character:FindFirstChild("HumanoidRootPart") then
			local mag = (i.Character.HumanoidRootPart.Position - root.Position).Magnitude
			if mag < dist then
				dist = mag
				closest = i.Character
			end
		end
	end

	return closest
end

remote.OnServerEvent:Connect(function(player)
	if debounce[player] then return end
	debounce[player] = true

	local character = player.Character
	if not character then return end

	local humanoid = character:FindFirstChild("Humanoid")
	local root = character:FindFirstChild("HumanoidRootPart")
	if not humanoid or not root then return end

	
	local grabSound = tool:FindFirstChild("GrabSound")
	if grabSound then
		local s = grabSound:Clone()
		s.Parent = root
		s:Play()
		game.Debris:AddItem(s, 3)
	end

	
	local grabAnim = tool:FindFirstChild("GrabAnim")
	local grabTrack
	if grabAnim then
		grabTrack = humanoid:LoadAnimation(grabAnim)
		grabTrack:Play()
	end

	
	local target = find_target(player)
	if not target then
		debounce[player] = nil
		return
	end

	local targetHum = target:FindFirstChild("Humanoid")
	local targetRoot = target:FindFirstChild("HumanoidRootPart")
	if not targetHum or not targetRoot then
		debounce[player] = nil
		return
	end

	
	humanoid.WalkSpeed = 0
	targetHum.WalkSpeed = 0


	local weld = Instance.new("Weld")
	weld.Part0 = root
	weld.Part1 = targetRoot
	weld.C0 = CFrame.new(0, 0, -3)
	weld.Parent = root


	local victimAnim = tool:FindFirstChild("VictimAnim")
	if victimAnim then
		local vt = targetHum:LoadAnimation(victimAnim)
		vt:Play()
	end

	
	task.wait(1.5)


	local slamSound = tool:FindFirstChild("SlamSound")
	if slamSound then
		local s = slamSound:Clone()
		s.Parent = root
		s:Play()
		game.Debris:AddItem(s, 3)
	end


	local slamAnim = tool:FindFirstChild("SlamAnim")
	if slamAnim then
		local slamTrack = humanoid:LoadAnimation(slamAnim)
		slamTrack:Play()
	end


	targetHum:TakeDamage(Damage)
	targetRoot.Velocity = root.CFrame.LookVector * 80 + Vector3.new(0, 30, 0)


	weld:Destroy()
	humanoid.WalkSpeed = 16
	targetHum.WalkSpeed = 16


	task.wait(Cooldown)
	debounce[player] = nil
end)