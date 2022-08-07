---
tags:
- EffectType
title: EFFECT_GRANT_RELIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_RELIC
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* RelicSource `Unknown`

## Samples
```SQL {title="GOODY_CULTURE_GRANT_ONE_RELIC"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_CULTURE_GRANT_ONE_RELIC",
		"MODIFIER_PLAYER_GRANT_RELIC",
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
		"GOODY_CULTURE_GRANT_ONE_RELIC",
		"Amount",
		1
	),
	(
		"GOODY_CULTURE_GRANT_ONE_RELIC",
		"RelicSource",
		"RELIC_SOURCE_TRIBAL_VILLAGE"
	);
	
```

