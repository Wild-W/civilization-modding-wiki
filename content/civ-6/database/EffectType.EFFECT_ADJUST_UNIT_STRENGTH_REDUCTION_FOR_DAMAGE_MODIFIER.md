---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_STRENGTH_REDUCTION_FOR_DAMAGE_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_STRENGTH_REDUCTION_FOR_DAMAGE_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="NATIONALIDENTITY_REDUCESTRENGTHREDUCTIONFORDAMAGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NATIONALIDENTITY_REDUCESTRENGTHREDUCTIONFORDAMAGE",
		"MODIFIER_PLAYER_UNITS_ADJUST_STRENGTH_REDUCTION_FOR_DAMAGE_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NATIONALIDENTITY_REDUCESTRENGTHREDUCTIONFORDAMAGE",
		"Amount",
		50
	);
	
```

