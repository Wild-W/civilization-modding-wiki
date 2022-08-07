---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_EMERGENCY_FAVOR_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_EMERGENCY_FAVOR_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Member `Boolean`

## Samples

```SQL {title="TRAIT_EMERGENCY_FAVOR_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_EMERGENCY_FAVOR_MODIFIER",
		"MODIFIER_PLAYER_ADJUST_EMERGENCY_FAVOR_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_EMERGENCY_FAVOR_MODIFIER",
		"Amount",
		100
	),
	(
		"TRAIT_EMERGENCY_FAVOR_MODIFIER",
		"Member",
		1
	);
	
```

