---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_POST_COMBAT_LOYALTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_POST_COMBAT_LOYALTY
>
> * Class: `PLAYERS`
> * Parameters:
>	* AdditionalGoldenAge `Unknown`
>	* AffectLocal `Boolean`
>		* If true\, the effect will apply to the victor's city\, if false it will apply to the enemy's city
>	* Amount `Integer`
>		* The delta amount to change the city's current Loyalty

## Samples

```SQL {title="TRAIT_DIMINISH_LOYALTY_IN_ENEMY_CITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_DIMINISH_LOYALTY_IN_ENEMY_CITY",
		"MODIFIER_PLAYER_ADJUST_POST_COMBAT_LOYALTY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_DIMINISH_LOYALTY_IN_ENEMY_CITY",
		"AdditionalGoldenAge",
		"-20"
	),
	(
		"TRAIT_DIMINISH_LOYALTY_IN_ENEMY_CITY",
		"AffectLocal",
		0
	),
	(
		"TRAIT_DIMINISH_LOYALTY_IN_ENEMY_CITY",
		"Amount",
		"-20"
	);
	
```

