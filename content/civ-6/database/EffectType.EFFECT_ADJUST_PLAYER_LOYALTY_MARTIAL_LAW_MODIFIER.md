---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_LOYALTY_MARTIAL_LAW_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_LOYALTY_MARTIAL_LAW_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_ADDITIONAL_MARTIAL_LAW"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADDITIONAL_MARTIAL_LAW",
		"MODIFIER_PLAYER_LOYALTY_ADJUST_MARTIAL_LAW_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADDITIONAL_MARTIAL_LAW",
		"Amount",
		5
	);
	
```

