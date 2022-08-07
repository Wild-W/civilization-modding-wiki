---
tags:
- EffectType
title: EFFECT_ADJUST_FLAT_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FLAT_BONUS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* BonusType `String`
>		* [GovernmentBonusNames.GovernmentBonusType]

## Samples

```SQL {title="AUTOCRACY_WONDERS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"AUTOCRACY_WONDERS",
		"MODIFIER_PLAYER_GOVERNMENT_FLAT_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AUTOCRACY_WONDERS",
		"Amount",
		10
	),
	(
		"AUTOCRACY_WONDERS",
		"BonusType",
		"GOVERNMENTBONUS_WONDER_CONSTRUCTION"
	);
	
```

