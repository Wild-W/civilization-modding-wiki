---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_RANDOM_CIVIC_BOOST_GOODY_HUT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_RANDOM_CIVIC_BOOST_GOODY_HUT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Source `String`
>		* CAPTURED_CITY

## Samples

```SQL {title="GOODY_CULTURE_GRANT_TWO_CIVIC_BOOSTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_CULTURE_GRANT_TWO_CIVIC_BOOSTS",
		"MODIFIER_PLAYER_GRANT_RANDOM_CIVIC_BOOST_GOODY_HUT",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOODY_CULTURE_GRANT_TWO_CIVIC_BOOSTS",
		"Amount",
		2
	);
	
```


```SQL {title="TRAIT_HELLENISTIC_FUSION_HOLY_SITE_INSPIRATION_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"TRAIT_HELLENISTIC_FUSION_HOLY_SITE_INSPIRATION_MODIFIER",
		"MODIFIER_PLAYER_GRANT_RANDOM_CIVIC_BOOST_GOODY_HUT",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_HELLENISTIC_FUSION_HOLY_SITE_INSPIRATION_MODIFIER",
		"Amount",
		1
	),
	(
		"TRAIT_HELLENISTIC_FUSION_HOLY_SITE_INSPIRATION_MODIFIER",
		"Source",
		"CAPTURED_CITY"
	);
	
```

