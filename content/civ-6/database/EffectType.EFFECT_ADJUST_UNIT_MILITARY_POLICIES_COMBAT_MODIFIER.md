---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_MILITARY_POLICIES_COMBAT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_MILITARY_POLICIES_COMBAT_MODIFIER
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples
```SQL {title="GORGO_POLICY_SLOT_COMBAT_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GORGO_POLICY_SLOT_COMBAT_BONUS",
		"MODIFIER_PLAYER_UNIT_ADJUST_PER_MILITARY_POLICIES_COMBAT_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GORGO_POLICY_SLOT_COMBAT_BONUS",
		"Amount",
		1
	);
	
```

