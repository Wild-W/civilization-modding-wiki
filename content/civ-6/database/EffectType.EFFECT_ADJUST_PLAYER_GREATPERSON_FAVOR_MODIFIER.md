---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_GREATPERSON_FAVOR_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_GREATPERSON_FAVOR_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_GREATPERSON_FAVOR_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_GREATPERSON_FAVOR_MODIFIER",
		"MODIFIER_PLAYER_ADJUST_GREATPERSON_FAVOR_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_GREATPERSON_FAVOR_MODIFIER",
		"Amount",
		50
	);
	
```

