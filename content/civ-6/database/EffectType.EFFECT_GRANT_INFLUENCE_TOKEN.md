---
tags:
- EffectType
title: EFFECT_GRANT_INFLUENCE_TOKEN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_INFLUENCE_TOKEN
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="CIVIC_AWARD_ONE_INFLUENCE_TOKEN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CIVIC_AWARD_ONE_INFLUENCE_TOKEN",
		"MODIFIER_PLAYER_GRANT_INFLUENCE_TOKEN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CIVIC_AWARD_ONE_INFLUENCE_TOKEN",
		"Amount",
		1
	);
	
```

