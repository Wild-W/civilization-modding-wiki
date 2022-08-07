---
tags:
- EffectType
title: EFFECT_GRANT_RANDOM_TECHNOLOGY_BOOST_ON_NEW_ERA
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_RANDOM_TECHNOLOGY_BOOST_ON_NEW_ERA
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* ApplyImmediately `Boolean`

## Samples

```SQL {title="HIGH_DIFFICULTY_FREE_TECH_BOOSTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId
	)
VALUES
	(
		"HIGH_DIFFICULTY_FREE_TECH_BOOSTS",
		"MODIFIER_PLAYER_GRANT_RANDOM_TECHNOLOGY_BOOST_ON_NEW_ERA",
		"PLAYER_IS_HIGH_DIFFICULTY_AI"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value,
		Extra
	)
VALUES
	(
		"HIGH_DIFFICULTY_FREE_TECH_BOOSTS",
		"Amount",
		"LinearScaleFromDefaultHandicap",
		0,
		1
	),
	(
		"HIGH_DIFFICULTY_FREE_TECH_BOOSTS",
		"ApplyImmediately",
		"ARGTYPE_IDENTITY",
		1,
		NULL
	);
	
```

