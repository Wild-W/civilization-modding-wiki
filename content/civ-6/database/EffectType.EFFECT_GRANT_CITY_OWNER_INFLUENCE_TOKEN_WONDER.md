---
tags:
- EffectType
title: EFFECT_GRANT_CITY_OWNER_INFLUENCE_TOKEN_WONDER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_CITY_OWNER_INFLUENCE_TOKEN_WONDER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="APADANA_AWARD_TWO_INFLUENCE_TOKEN_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APADANA_AWARD_TWO_INFLUENCE_TOKEN_MODIFIER",
		"MODIFIER_PLAYER_GRANT_INFLUENCE_TOKEN_FROM_CITY_WONDER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APADANA_AWARD_TWO_INFLUENCE_TOKEN_MODIFIER",
		"Amount",
		2
	);
	
```

