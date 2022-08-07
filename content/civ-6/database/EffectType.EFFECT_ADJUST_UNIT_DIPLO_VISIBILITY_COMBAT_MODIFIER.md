---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_DIPLO_VISIBILITY_COMBAT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_DIPLO_VISIBILITY_COMBAT_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* DeltaWithOpponent `Boolean`

## Samples

```SQL {title="TRAIT_EACH_DIPLO_VISIBILITY_COMBAT_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_EACH_DIPLO_VISIBILITY_COMBAT_MODIFIER",
		"MODIFIER_PLAYER_UNITS_ADJUST_DIPLO_VISIBILITY_COMBAT_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_EACH_DIPLO_VISIBILITY_COMBAT_MODIFIER",
		"Amount",
		3
	),
	(
		"TRAIT_EACH_DIPLO_VISIBILITY_COMBAT_MODIFIER",
		"DeltaWithOpponent",
		1
	);
	
```

